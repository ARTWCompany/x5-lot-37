
install-app:
	# Install APP Kubernetes cluster 
	# NameSpace + ConfigMap + Ingress
	kubectl apply -f ns.yml
	kubectl apply -f config_map.yml 
	kubectl apply -f registry.yml
	kubectl apply -f ingress.yml
	# Start Postgresql 
	kubectl apply -f postgres.yml 
	# Start migration DataBase 
	kubectl apply -f colstatik.yml
	kubectl apply -f migrate.yml

	# Start Frontend , Backend 
	kubectl apply -f django.yml
	kubectl apply -f frontend.yml
	

clean-app:
	kubectl delete ns x5-lot37

