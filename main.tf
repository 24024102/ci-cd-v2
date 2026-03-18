provider "aws" {
  region = "us-east-1" 
}
data "aws_ami" "ubuntu" {
    most_recent = true
    filter {
        name = "name"
        values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
    }
    filter {
        name = "virtualization-type"
        values = ["hvm"]
    }
    owners = ["099720109477"]
}

resource "aws_security_group" "web_sg" {
    name      = "fastapi_web_sg"
    description     = "Allow HTTP web trafic"
    ingress {
    description = "Allow HTTP from anywhere"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Пускаем всех
  }

  egress {
    description = "Allow all outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "web_server" {
    ami      = data.aws_ami.ubuntu.id
    instance_type    = "t2.micro"

    vps_security_group_ids   = [aws_security_group.web_sg.id]
    user_data = <<- EQF
                 #!/bin/bash
                 sudo apt-get update
                 sudo apt-get install -y docker.io
                 sudo systemctl start docker
                 sudo systemctl enable docker 
                 sudo docker run -d -p 80:80 24024102/ci-cd-v2:latest
                 EQF


tags = {
    Name = "FastAPI-Prod-Server"
  }
}


output "server_public_ip" {
  description = "Public IP address of the web server"
  value       = aws_instance.web_server.public_ip
}
