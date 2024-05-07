The ORY Kratos HTTP Public API is available via:
  export POD_NAME=$(kubectl get pods --namespace ory -l "app.kubernetes.io/name=kratos,app.kubernetes.io/instance=kratos" -o jsonpath="{.items[0].metadata.name}")
  echo "Visit http://127.0.0.1:80 to use your application"
  kubectl port-forward $POD_NAME 80:4433
  export KRATOS_PUBLIC_URL=http://127.0.0.1:80


If you have the ORY Kratos CLI installed locally, you can run commands
against this endpoint:

  kratos ... $KRATOS_PUBLIC_URL

The ORY Kratos HTTP Admin API is available via:
  export POD_NAME=$(kubectl get pods --namespace ory -l "app.kubernetes.io/name=kratos,app.kubernetes.io/instance=kratos" -o jsonpath="{.items[0].metadata.name}")
  echo "Visit http://127.0.0.1:80 to use your application"
  kubectl port-forward $POD_NAME 80:4434
  export KRATOS_ADMIN_URL=http://127.0.0.1:80

If you have the ORY Kratos CLI installed locally, you can run commands
against this endpoint:

  kratos ... $KRATOS_ADMIN_URL

