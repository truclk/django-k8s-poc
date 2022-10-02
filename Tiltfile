# Enable helm and setup kafka:
namespace = "upload-service"
service_name = "upload-service"

load("ext://helm_remote", "helm_remote")
load('ext://syncback', 'syncback')


helm_remote(
    "postgresql",
    namespace=namespace,
    repo_name="bitnami",
    release_name="postgresql",
    repo_url="https://charts.bitnami.com/bitnami",
    values="charts/values-dev-postgresql.yaml",
    version="11.0.6"
)


syncback(
    name="syncback-upload-service",
    k8s_object="deploy/upload-service",
    src_dir="/workspace/",
    target_dir="upload_project/",
    namespace=namespace,
)



# Build repo:
docker_build(
    "upload-service",
    ".",
    build_args={"debug": "true"},
    live_update=[sync("./upload_project", "/workspace")],
    entrypoint="echo 'WARNING: container is running in dev mode. Entrypoint is overriden in Tiltfile'; sleep 9999999999"
)
repo_deployment = k8s_yaml(helm("./charts/upload-service", name=service_name, namespace=namespace))

test(
    "test-everything",
    "make test",
    deps=["./upload_project/"],
    trigger_mode=TRIGGER_MODE_MANUAL,
    resource_deps=[service_name, "postgresql"],
)

# # Setup prometheus
# load(
#     'ext://coreos_prometheus',
#     'setup_monitoring',
#     'get_prometheus_resources',
#     'get_prometheus_dependencies',
# )
# setup_monitoring()
# k8s_resource(
#     'upload_service',
#     objects=get_prometheus_resources(repo_deployment, 'upload-service'),
#     resource_deps=get_prometheus_dependencies(),
# )
k8s_resource(service_name, port_forwards="8885:8000")

