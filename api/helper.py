import base64

from io import BytesIO
from PIL import Image
import requests
import urllib

def image_to_byte_array(image: Image) -> bytes:
    # BytesIO is a file-like buffer stored in memory
    imgByteArr = BytesIO()
    # image.save expects a file-like as a argument
    image.save(imgByteArr, format=image.format)
    # Turn the BytesIO object back into a bytes object
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr


def uploadImageToIPFS(image_url):
    # Get image
    image_raw = requests.get(image_url, stream=True).raw
    image_object = Image.open(image_raw)

    # bytes to string
    image_byte = image_to_byte_array(image_object)
    # image_byte = base64.b64encode(image_byte)
    # image_str = image_byte.decode('utf-8')

    # # string to bytes
    # new_img_byte = image_str.encode(encoding='utf-8')
    # new_img_byte = base64.b64decode(new_img_byte)

    # context = ssl._create_unverified_context()
    # with urlopen(image_url, context=context) as url:
    #     with open('temp.jpg', 'wb') as f:
    #         f.write(url.read())

    # Upload NFT Metadata to Pinata
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    payload = {'pinataOptions': '{"cidVersion": 1}',
               'pinataMetadata': '{"name": "MyFile", "keyvalues": {"company": "Pinata"}}'}
    files = [
        ('file', ('temp.jpg', base64.b64encode(image_byte), 'application/octet-stream'))
    ]
    headers = {
        'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiJmNjJkNzk2Yi1lZTJlLTQyZDEtYTRiNS1kZWY3MzY5OWY0YTAiLCJlbWFpbCI6ImthdTk2a2ltQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJwaW5fcG9saWN5Ijp7InJlZ2lvbnMiOlt7ImlkIjoiRlJBMSIsImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxfSx7ImlkIjoiTllDMSIsImRlc2lyZWRSZXBsaWNhdGlvbkNvdW50IjoxfV0sInZlcnNpb24iOjF9LCJtZmFfZW5hYmxlZCI6ZmFsc2UsInN0YXR1cyI6IkFDVElWRSJ9LCJhdXRoZW50aWNhdGlvblR5cGUiOiJzY29wZWRLZXkiLCJzY29wZWRLZXlLZXkiOiI3YWVjNDY3NWI3NGZlY2U1YjU3YyIsInNjb3BlZEtleVNlY3JldCI6IjY5OTFiM2ZiYTUyNjZlZTBiNDJmOTA2ZThiZmVhNDlkZmUxYTAwM2ExMmM1ODY1ZTA2YWM3YzFkYTBkNzBmYTgiLCJpYXQiOjE2NzM5NDI4ODB9.yMa-D0nlaNpZVANGtYVxl-o0DbjcPYle-4YJFMnCfCI'
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    return response

