import os
from os import listdir
from tempfile import NamedTemporaryFile, TemporaryDirectory

from aiogram.types import Message, MediaGroup, InputFile
from instascrape import Post


class Insta:
    def __init__(self, message: Message):
        self.message = message

    async def _video_post(self, post: Post):
        with NamedTemporaryFile(suffix='.mp4', mode="wb+") as fp:
            post.download(fp.name)
            await self.message.answer_video(fp.file)

    async def _photo_post(self, post: Post):
        with NamedTemporaryFile(suffix='.png', mode="wb+") as fp:
            post.download(fp.name)
            await self.message.answer_photo(fp.file)

    async def _carousel_post(self, post: Post):
        with TemporaryDirectory() as dir:
            media = MediaGroup()
            post.download_carousel(outdir=dir)
            for file in listdir(dir):
                extension = file.split('.')[-1]
                abs_path = os.path.abspath(os.path.join(dir, file))
                if extension in ["jpg", "jpeg", "png"]:
                    media.attach_photo(InputFile(abs_path))
                elif extension == 'mp4':
                    media.attach_video(InputFile(abs_path))
            await self.message.answer_media_group(media)

    async def get_data(self):
        post = Post(self.message.text)
        post.scrape()
        if post.parse_carousel_urls():
            await self._carousel_post(post)
        elif post.is_video:
            await self._video_post(post)
        else:
            await self._photo_post(post)
