library(dplyr)

df <- read.table("Day_2/input.txt") %>%
  group_by(V1) %>%
  summarise(sum = sum(V2))

depth <- df[[1,2]]-df[[3,2]]
horizontal <- df[[2,2]]

cat("Depth of: ", depth)
cat("Horizontal of", horizontal)
cat("Product of", depth*horizontal)