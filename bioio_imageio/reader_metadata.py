#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import List

import bioio_base.reader_metadata

###############################################################################


class ReaderMetadata(bioio_base.reader_metadata.ReaderMetadata):
    """
    Notes
    -----
    Defines metadata for the reader itself (not the image read),
    such as supported file extensions.
    """

    @staticmethod
    def get_supported_extensions() -> List[str]:
        """
        Return a list of file extensions this plugin supports reading.
        """
        # See ever growing list from imageio
        # https://imageio.readthedocs.io/en/stable/formats/index.html
        return [
            "264",
            "265",
            "3fr",
            "3g2",
            "A64",
            "IMT",
            "MCIDAS",
            "PCX",
            "SPIDER",
            "XVTHUMB",
            "a64",
            "adp",
            "amr",
            "amv",
            "apng",
            "arw",
            "asf",
            "avc",
            "avi",
            "avs",
            "avs2",
            "bay",
            "bif",
            "bmp",
            "cdg",
            "cgi",
            "cif",
            "ct",
            "dcr",
            "dib",
            "dip",
            "dng",
            "dnxhd",
            "dv",
            "dvd",
            "erf",
            "exr",
            "fff",
            "gif",
            "icb",
            "if",
            "iiq",
            "ism",
            "jif",
            "jfif",
            "jng",
            "jp2",
            "jpg",
            "mov",
            "mp4",
            "mpo",
            "msp",
            "pdf",
            "png" "ppm",
            "ps",
            "zif",
        ]

    @staticmethod
    def get_reader() -> bioio_base.reader.Reader:
        """
        Return the reader this plugin represents
        """
        from .reader import Reader

        return Reader
