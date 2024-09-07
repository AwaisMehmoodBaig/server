provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "server" {
  ami           = "ami-066784287e358dad1"
  instance_type = "t2.micro"
  tags = {
    Name = "server_terraform"
  }
}

resource "aws_instance" "client" {
  ami           = "ami-066784287e358dad1"
  instance_type = "t2.micro"
  tags = {
    Name = "client_terraform"
  }
}

