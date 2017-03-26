/*
    Copyright 2017 Daniel Harding

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#include <stdlib.h>

#include <png.h>
#include "lib/quirc.h"

#pragma warning(disable:4996)

int load_png(struct quirc *q, const char *filename)
{
    int width, height, rowbytes, interlace_type, number_passes = 1;
    png_uint_32 trns;
    png_byte color_type, bit_depth;
    png_structp png_ptr = NULL;
    png_infop info_ptr = NULL;
    FILE *infile = NULL;
    uint8_t *image;
    int ret = -1;
    int pass;

    if ((infile = fopen(filename, "rb")) == NULL)
        goto out;

    png_ptr = png_create_read_struct(PNG_LIBPNG_VER_STRING, NULL, NULL, NULL);
    if (!png_ptr)
        goto out;

    info_ptr = png_create_info_struct(png_ptr);
    if (!info_ptr)
        goto out;

    if (setjmp(png_jmpbuf(png_ptr)))
        goto out;

    png_init_io(png_ptr, infile);

    png_read_info(png_ptr, info_ptr);

    color_type = png_get_color_type(png_ptr, info_ptr);
    bit_depth = png_get_bit_depth(png_ptr, info_ptr);
    interlace_type = png_get_interlace_type(png_ptr, info_ptr);

    // Read any color_type into 8bit depth, Grayscale format.
    // See http://www.libpng.org/pub/png/libpng-manual.txt

    // PNG_COLOR_TYPE_GRAY_ALPHA is always 8 or 16bit depth.
    if (color_type == PNG_COLOR_TYPE_GRAY && bit_depth < 8)
        png_set_expand_gray_1_2_4_to_8(png_ptr);

    if ((trns = png_get_valid(png_ptr, info_ptr, PNG_INFO_tRNS)))
        png_set_tRNS_to_alpha(png_ptr);

    if (bit_depth == 16)
#if PNG_LIBPNG_VER >= 10504
        png_set_scale_16(png_ptr);
#else
        png_set_strip_16(png_ptr);
#endif

    if ((trns) || color_type & PNG_COLOR_MASK_ALPHA)
        png_set_strip_alpha(png_ptr);

    if (color_type == PNG_COLOR_TYPE_PALETTE)
        png_set_palette_to_rgb(png_ptr);

    if (color_type == PNG_COLOR_TYPE_PALETTE ||
        color_type == PNG_COLOR_TYPE_RGB ||
        color_type == PNG_COLOR_TYPE_RGB_ALPHA) {
        png_set_rgb_to_gray_fixed(png_ptr, 1, -1, -1);
    }

    if (interlace_type != PNG_INTERLACE_NONE)
        number_passes = png_set_interlace_handling(png_ptr);

    png_read_update_info(png_ptr, info_ptr);

    width = png_get_image_width(png_ptr, info_ptr);
    height = png_get_image_height(png_ptr, info_ptr);
    rowbytes = png_get_rowbytes(png_ptr, info_ptr);
    if (rowbytes != width) {
        fprintf(stderr,
            "load_png: expected rowbytes to be %u but got %u\n",
            width, rowbytes);
        goto out;
    }

    if (quirc_resize(q, width, height) < 0)
        goto out;

    image = quirc_begin(q, NULL, NULL);

    for (pass = 0; pass < number_passes; pass++) {
        int y;

        for (y = 0; y < height; y++) {
            png_bytep row_pointer = image + y * width;
            png_read_rows(png_ptr, &row_pointer, NULL, 1);
        }
    }

    png_read_end(png_ptr, info_ptr);

    ret = 0;
    /* FALLTHROUGH */
out:
    /* cleanup */
    if (png_ptr) {
        if (info_ptr)
            png_destroy_read_struct(&png_ptr, &info_ptr, (png_infopp)NULL);
        else
            png_destroy_read_struct(&png_ptr, (png_infopp)NULL, (png_infopp)NULL);
    }
    if (infile)
        fclose(infile);
    return (ret);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        return -1;
    }

    struct quirc *qr;

    qr = quirc_new();
    if (!qr) {
        //perror("Failed to allocate memory");
        abort();
    }

    int status = -1;
    status = load_png(qr, argv[1]);
    if (status < 0) {
        quirc_destroy(qr);
        return -1;
    }

    quirc_end(qr);

    int num_codes;
    int i;

    num_codes = quirc_count(qr);
    if (num_codes > 0) {
        FILE* outfile = NULL;
        if ((outfile = fopen("script.frodo", "w")) != NULL) {
            for (i = 0; i < num_codes; i++) {
                struct quirc_code code;
                struct quirc_data data;
                quirc_decode_error_t err;

                quirc_extract(qr, i, &code);

                /* Decoding stage */
                err = quirc_decode(&code, &data);
                if (err) {
                    //printf("DECODE FAILED: %s\n", quirc_strerror(err));
                }
                else {
                    //printf("Data: %s\n", data.payload);
                    fprintf(outfile, "%s\n", data.payload);
                }
            }
            fclose(outfile);
        }
    }

    quirc_destroy(qr);
    return 0;
}