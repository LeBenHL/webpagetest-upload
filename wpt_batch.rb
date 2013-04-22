require 'phash/image'

image1 = ARGV[0]
image2 = ARGV[1]

puts Phash::Image.new(image1) % Phash::Image.new(image2)