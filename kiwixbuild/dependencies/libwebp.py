import os

from .base import (
    Dependency,
    ReleaseDownload,
    MakeBuilder,
)

from kiwixbuild.utils import Remotefile, pj, Defaultdict, SkipCommand, run_command
from kiwixbuild._global import get_target_step

class LibWebp(Dependency):
    name = "libwebp"

    class Source(ReleaseDownload):
        name = "libwebp"
        archive = Remotefile('libwebp-1.2.4.tar.gz',
                             '7bf5a8a28cc69bcfa8cb214f2c3095703c6b73ac5fba4d5480c205331d9494df',
                             'https://storage.googleapis.com/downloads.webmproject.org/releases/webp/libwebp-1.2.4.tar.gz')

    class Builder(MakeBuilder):
        configure_option = " ".join(
            ["--disable-{}".format(p)
                for p in ('shared')])
