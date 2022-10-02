# upload-service

This is a PoC about running Django application inside kubernetes.

This appplication would simple upload photo with metadata.

Because K8S pod is stateless. We would use S3 as the service to store actual file. 
1. Client request API to get secret upload link 
2. client uploaded image to S3 storage.
3. client actual save the image with metadata

Improvement:
- We can implement captcha to increase security and prevent flooding.
- We can implement a job to clean any requested upload model or deleted photo

## Requirements:

- Tilt [tilt.dev](https://tilt.dev)
- Helm [helm.sh](https://helm.sh/)
- kubectl connected to any k8s cluster. Example is using [k3d](https://k3d.io/v5.1.0/)
- make

## Setup

Use any k8s cluster provider. This example would be using [k3d](https://k3d.io/).

    # Launch cluster
    make dev_infra

    # Launch stack
    make run

    # Run HTTP server
    make devserver
