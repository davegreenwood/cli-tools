# Python CLI tools

A docker image with some python CLI tools.

## Building the image

1. Create a new builder instance:

```shell
docker buildx create --name mybuilder --use
```

2. Build and push the multi-architecture image:

```shell
docker buildx build --platform linux/amd64,linux/arm64 -t dgrnwd/cli-tools:latest --push .
```

3. Run the image:

```shell
docker run -it dgrnwd/cli-tools:latest
```

## QR code generator

Generate a QR code from a string, and save it to a file.

```shell
docker run --rm \
    -v "$(PWD)":/workspace \
    -w /workspace \
    dgrnwd/cli-tools:latest \
    python /app/qr.py "Your data here" "qr.png"
```

Make an alias in your `.bashrc` or `.zshrc`:

```shell
alias qr='docker run --rm -v "$(PWD)":/workspace -w /workspace dgrnwd/cli-tools:latest python /app/qr.py'
```

Now you can generate a QR code with:

```shell
qr "Your data here" "qr.png"
```
