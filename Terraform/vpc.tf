resource "aws_vpc" "main" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "murali-vpc"
  }
}

# second vpc in aws

resource "aws_vpc" "main-2" {
  cidr_block       = "10.0.0.0/16"
  instance_tenancy = "default"

  tags = {
    Name = "murali-vpc-2"
  }
}

# public subnet

resource "aws_subnet" "main-pub-sub" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "murali-pub-subnet"
  }
}

# private subnet

resource "aws_subnet" "main-prvt-sub" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "10.0.2.0/24"
  availability_zone = "us-east-1b"

  tags = {
    Name = "murali-prvt-subnet"
  }
}

# internet gateway

resource "aws_internet_gateway" "gw" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "murali-igw-new"
  }
}