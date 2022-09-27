# reads image service text if num then writes path of image using random number to image-server text

# While true:
# Sleep for 1 second
# Open image-service.txt
# if(read image-service.txt == type(number))
# copy number to local variable
# Use Mod operator to mod number with number of images
# Write path (ex : /users/cs361-images/{number}.jpg) to image-service.txt
# Close file image-service.txt