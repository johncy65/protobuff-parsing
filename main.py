def set_config(num_classes, batch_size, num_steps):
    template = "template.txt"
    file = open(template, "r")
    string = file.read()
    string = string.replace("#num_classes#", str(num_classes), 1)
    string = string.replace("#batch_size#", str(batch_size), 1)
    string = string.replace("#num_steps#", str(num_steps), 1)
    file2 = open("f.config", "w")
    file2.write(string)
    file2.close()
    file.close()

set_config(40,5,3000)