provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_project_service" "services" {
  for_each = toset([
    "run.googleapis.com",
    "bigquery.googleapis.com",
    "aiplatform.googleapis.com",
    "firebase.googleapis.com"
  ])
  service = each.key
}

resource "google_bigquery_dataset" "worksphere" {
  dataset_id = "worksphere360"
  location   = "US"
}

resource "google_cloud_run_service" "backend" {
  name     = "worksphere360-api"
  location = var.region

  template {
    spec {
      containers {
        image = var.backend_image
        env {
          name  = "BQ_DATASET"
          value = google_bigquery_dataset.worksphere.dataset_id
        }
      }
    }
  }
}
