class VideoFile:
    def __init__(self, res):
        self.file = res

    def save(self):
        print("Saving file... Done!")


class OggCompressionCodec:
    pass


class MPEG4CompressionCodec:
    pass


class CodecFactory:
    @staticmethod
    def extract(file):
        print("Codec factory extracting file... Done!")
        return "mp4"


class BitrateReader:
    @staticmethod
    def read(file, codec):
        print("Bitrate reader reading file... Done!")
        return "fake buffer"

    @staticmethod
    def convert(buffer, codec):
        print("Bitrate reader converting file... Done!")
        return "fake result"


class AudioMixer:
    @staticmethod
    def fix(result):
        print("Audio mixer fixing audio... Done!")
        return "fake result"


class VideoConverter:
    def convert(self, filename, format):
        file = VideoFile(filename)
        src_codec = CodecFactory.extract(file)
        if format == "mp4":
            dest_codec = MPEG4CompressionCodec()
        else:
            dest_codec = OggCompressionCodec()
        buffer = BitrateReader.read(filename, src_codec)
        result = BitrateReader.convert(buffer, dest_codec)
        result = AudioMixer().fix(result)
        return VideoFile(result)


def client_code():
    convertor = VideoConverter()
    mp4 = convertor.convert("funny-cats-video.ogg", "mp4")
    mp4.save()


if __name__ == '__main__':
    client_code()
