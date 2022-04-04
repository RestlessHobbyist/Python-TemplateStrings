from string import Template

# Typical string formatting with format()
str1 = "Some silly string written by {0} for {1}.".format("me", "shits'n giggles")
print(str1)

templ = Template("Well well, look what the ${animal} dragged in. Didn't think I'd see your ${adjective} mug again")

str2 = templ.substitute(animal="capybara",adjective="clockwise")
print(str2)

data = {
  "animal":"mongoose",
  "adjective":"burly"
}

str3 = templ.substitute(data)
print(str3)