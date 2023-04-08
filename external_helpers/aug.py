import os
import shutil
import random
import torchvision.transforms as transforms
from PIL import Image

# Define the directories for the original and augmented data
directory = 'data'
balanced_dir = 'balanced_data'

# Define the number of images to have per class
num_images_per_class = 1200

# Create the balanced directory if it doesn't exist
if not os.path.exists(balanced_dir):
    os.makedirs(balanced_dir)

transform = transforms.Compose([
    # transforms.Grayscale(num_output_channels=3),
    transforms.RandomApply([transforms.RandomHorizontalFlip()], p=0.5),
    transforms.RandomApply([transforms.RandomRotation(1)], p=0.25),
    transforms.RandomApply([transforms.RandomCrop(2, padding=1)], p=0.25),
    transforms.RandomApply([transforms.ColorJitter(brightness=0.2, contrast=0.25, saturation=0.125, hue=0.25)], p=0.5),
    transforms.RandomApply([transforms.ColorJitter(brightness=0.2, contrast=0.25, saturation=0.125, hue=0.25)], p=0.15),
    transforms.RandomApply([transforms.RandomAffine(degrees=10, translate=(0.1, 0.1), scale=(0.9, 1.1), shear=5)], p=0.25),
    transforms.RandomApply([transforms.RandomPerspective(distortion_scale=0.2, p=0.25)], p=0.25)
])

# Loop over the classes
for class_name in os.listdir(directory):
    class_dir = os.path.join(directory, class_name)
    balanced_class_dir = os.path.join(balanced_dir, class_name)
    
    # Create the balanced class directory if it doesn't exist
    if not os.path.exists(balanced_class_dir):
        os.makedirs(balanced_class_dir)
    
    # Get the number of images in the class directory
    num_images = len(os.listdir(class_dir))
    
    # If the class has fewer images than the required number of images, generate new images
    if num_images < num_images_per_class:
        num_augmented_images = num_images_per_class - num_images
        
        # Loop over the images in the class directory and generate new augmented images
        for i, image_name in enumerate(os.listdir(class_dir)):
            if i >= num_images:
                break
            image_path = os.path.join(class_dir, image_name)
            image = Image.open(image_path)
            
            # Save the original image to the balanced class directory
            balanced_image_path = os.path.join(balanced_class_dir, image_name)
            shutil.copy(image_path, balanced_image_path)
            
        for i in range(num_augmented_images):
            image_name = f"{class_name}_{i}.jpg"
            image_path = os.path.join(class_dir, random.choice(os.listdir(class_dir)))
            image = Image.open(image_path)
            
            # Convert the image to an RGB image and remove the alpha channel
            image = image.convert('RGB')
            image = image.crop((0, 0, image.width, image.height - 1))
            
            # Apply the transformations to the image
            augmented_image = transform(image)
            
            # Save the augmented image to the balanced class directory
            balanced_image_path = os.path.join(balanced_class_dir, image_name)
            augmented_image.save(balanced_image_path)
            
    # If the class has more images than the required number of images, randomly select images to copy
    else:
        random_image_names = random.sample(os.listdir(class_dir), num_images_per_class)
        for image_name in random_image_names:
            image_path = os.path.join(class_dir, image_name)
            balanced_image_path = os.path.join(balanced_class_dir, image_name)
            shutil.copy(image_path, balanced_image_path)
