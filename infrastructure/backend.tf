terraform {
  backend "gcs" {
    bucket = "tf_state_bucket_demo"
    prefix = "terraform/state"
  }
}
