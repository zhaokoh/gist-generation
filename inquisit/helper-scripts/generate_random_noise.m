random_colour_image = rand(1080, 1920, 3);
imwrite(random_colour_image, 'random_colour_image.jpg', 'jpg');

greyscale_image = rand(1080, 1920);
imwrite(greyscale_image, 'random_greyscale_image.jpg', 'jpg');

