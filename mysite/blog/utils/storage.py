from storages.backends.s3boto3 import S3Boto3Storage

class Ckeditor5S3Storage(S3Boto3Storage):
    location = 'blog/media'
    file_overwrite = False