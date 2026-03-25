variable "aws_region" {
  type    = string
  default = "eu-central-1"
}

variable "cluster_name" {
  type    = string
  default = "fastapi-eks"
}

variable "ecr_repository_name" {
  type    = string
  default = "fastapi-app"
}

variable "node_group_name" {
  type    = string
  default = "ng-1"
}

variable "github_owner" {
  type = string
}

variable "github_repo" {
  type = string
}

variable "github_branch" {
  type    = string
  default = "main"
}