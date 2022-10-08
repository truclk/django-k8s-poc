
run: create_namespace
	TILT_PORT=10350 tilt up
down:
	tilt down

create_namespace:
	kubectl create namespace upload-service || true

dev_infra: infra install_precommit
ci_infra: infra

infra:
	k3d cluster create dev-local --registry-create dev-local-registry:127.0.0.1:5001 --kubeconfig-update-default --kubeconfig-switch-context --api-port 0.0.0.0:50956

exec:
	kubectl exec -n upload-service -it deploy/upload-service -- bash


test:
	kubectl exec -n upload-service -it deploy/upload-service -- pytest -n 4

server:
	kubectl exec -n upload-service -it deploy/upload-service -- python3 main.py

install_precommit:
	pre-commit install > /dev/null

migrate:
	kubectl exec -n upload-service -it deploy/upload-service -- ./manage.py migrate

migrations:
	kubectl exec -n upload-service -it deploy/upload-service -- ./manage.py makemigrations
	sleep 1
	TILT_PORT=10350 tilt trigger syncback-upload-service


