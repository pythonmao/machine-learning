import image_mgt

image_mgt.grayscale("./test.jpeg", "/home/sourceCode/AI/complete")


image_mgt.rotate("./test1.jpeg", "/home/sourceCode/AI/complete", 30, expand=0)

image_mgt.mirror("./test2.jpeg", "/home/sourceCode/AI/complete", 0)

image_mgt.squash("./test3.jpeg", "/home/sourceCode/AI/complete", 100, 100)

image_mgt.zoom("./test4.jpeg", "/home/sourceCode/AI/complete", 300, 300)

image_mgt.crop("./test5.jpeg", "/home/sourceCode/AI/complete", 50, 50)

image_mgt.fill("./test6.jpeg", "/home/sourceCode/AI/complete", 300, 300)

image_mgt.half_fill_half_crop("./test7.jpeg", "/home/sourceCode/AI/complete", 500, 500)

image_mgt.shift("./test8.jpeg", "/home/sourceCode/AI/complete", 100, 100)

image_mgt.colorize("./test9.jpeg", "/home/sourceCode/AI/complete", (10,100,200), (10,100,200))
