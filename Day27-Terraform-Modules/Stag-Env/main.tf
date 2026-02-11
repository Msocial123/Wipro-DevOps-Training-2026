# call child module vpc

module "vpc" {
    source = "./modules/vpc"
    vpc_cidr_blcok = var.vpc_cidr_blcok
    instance_tenancy = var.instance_tenancy
    vpc_name = var.vpc_name
}

# call child module subnet

module "subnet" {
    source = "./modules/subnet"
    pub_subnet_cidr_block = var.pub_subnet_cidr_block
    pub_subnet_az = var.pub_subnet_az
    pub_subnet_name = var.pub_subnet_name
    vpc_id = module.vpc.vpc_id
}