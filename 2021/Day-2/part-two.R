df <- read.table("Day_2/input.txt")


aim <- 0
depth <- 0 
horizontal <- 0

for(row in as.list(as.data.frame(t(df)))){
  direction <- row[1]
  value <- as.integer(row[2])
  if(direction=="forward"){
    horizontal <- horizontal + value
    depth <- depth+aim*value
  }
  else{
    if(direction=="down"){
      aim <- aim + value
    }
    else{
      aim <- aim - value
    }
  }
}

cat("Depth of: ", depth)
cat("Horizontal of", horizontal)
cat("Product of", depth*horizontal)