# importing modules
from pathlib import Path
import cv2
import os

# creating class
class file_handling():

    # creating function to save images
    def save_images(self, save_path, img, counter: int):

        # creating path objects
        path = save_path 
        filename = f'{counter}.jpg'
        
        file_path = os.path.join(path, filename) # defining file path

        cv2.imwrite(file_path, img) # saving image

        print(f'{filename} saved in {save_path}')
    
    # creating function to generate image from images
    def img_to_video(self, images_path: str, video_save_path: str, file_name: str):

        # creating save path if it does not exist
        if not os.path.exists(video_save_path):
            os.mkdir(video_save_path)

        # defining video name and video path
        video_name = f'{file_name}.mp4' 
        video_path = video_save_path

        filename = os.path.join(video_path, video_name) # creating video file path

        # sorting the images in ascending order to generate smooth videos
        sorted_images = []
        img_path = Path(images_path)
        images = list(img_path.glob('*.jpg')) # accessuing the files with '.jpg' extension

        # sorting loop
        for image in images:
            sorted_images.append(int(image.stem))
            sorted_images.sort()

        image_files = []

        # modifying image names after sorting
        for name in sorted_images:
            file_name = f'{name}.jpg'
            filepath = os.path.join(img_path, file_name)
            image_files.append(filepath)


        first_img = cv2.imread(image_files[0]) # getting first image
        
        # getting image shape
        size = list(first_img.shape)
        del size[2]
        size.reverse()

        # setting up video writer
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video = cv2.VideoWriter(filename, fourcc, 20, size)

        # creating video from images
        for image in image_files:
            frame = cv2.imread(image)
            video.write(frame)
            
        print(f'video saved in {video_save_path} as {video_name}')

        video.release()
        cv2.destroyAllWindows()