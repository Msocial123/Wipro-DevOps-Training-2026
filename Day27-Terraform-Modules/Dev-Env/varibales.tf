# vpc varibles

variable "vpc_cidr_blcok" {
  description = "this is for vpc cidr block"
}

variable "instance_tenancy" {
  description = "this is vpc tenancy name"
}

variable "vpc_name" {
  description = "this is a vpc name"
}

# public subnet variables

variable "pub_subnet_cidr_block" {
  description = "this is for public subnet cidr block"
}

variable "pub_subnet_az" {
  description = "this is for public subnet availability zone"  
}

variable "pub_subnet_name" {
  description = "this is for public subnet name"  
}

# provider variables

variable "dev_env_region" {
  description = "this is for Dev Env region"
}