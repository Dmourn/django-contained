
CONTAINER_LIST = nginx-alpine api-test
export CONTAINER_CMD=podman

.PHONY: $(CONTAINER_LIST)

containers: 
	@for image in $(CONTAINER_LIST); do \
		$(MAKE) -C $$image ; \
	done
	
clean:
	podman pod rm -f testpod
	${CONTAINER_CMD} system prune

clean-all: clean
	${CONTAINER_CMD} rmi $(CONTAINER_LIST)
