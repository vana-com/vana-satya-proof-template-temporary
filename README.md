# Vana Satya Proof of Contribution Python Template

This repository serves as a template for creating proof tasks using Python and Gramine for secure computation.

## Overview

This template provides a basic structure for building proof tasks that:

1. Read input files from the `/input` directory
2. Process the data
3. Write proof results to the `/output` directory

The project is designed to work with Gramine, allowing the code to run in a secure enclave.

## Getting Started

To use this template:

1. Fork this repository
2. Modify the `src/main.py` file to implement your specific proof logic
3. Update the `python.manifest.template` if you need to add any additional files or change the configuration
4. Commit your changes and push to your repository

## Local Development

To run the proof locally, without Gramine, you can use Docker:

    ```
    docker build -t my-proof .
    docker run \
    --rm \
    --volume $(pwd)/demo/sealed:/sealed \
    --volume $(pwd)/demo/input:/input \
    --volume $(pwd)/demo/output:/output \
    my-proof
    ```

## Building and Releasing

This template includes a GitHub Actions workflow that automatically:

1. Builds a Docker image with your code
2. Creates a Gramine-shielded container (GSC) image
3. Publishes the GSC image as a GitHub release

To use this workflow, you need to:

1. Set up a signing key as a GitHub secret named `SIGNING_KEY`
2. Push your changes to the `main` branch or create a pull request

## Running with SGX

To run your application:

   ```
    docker run \
    --rm \
    --volume /gsc-my-proof/input:/input \
    --volume /gsc-my-proof/output:/output \
    gsc-my-proof
   ```

If you wish to use Gramine-enabled SGX features like sealing, remote attestation, etc., you may need to mount additional volumes and devices:

   ```
    docker run \
    --rm \
    --volume /gsc-my-proof/input:/input \
    --volume /gsc-my-proof/output:/output \
    --device /dev/sgx_enclave:/dev/sgx_enclave \
    --volume /var/run/aesmd:/var/run/aesmd \
    --volume /mnt/gsc-my-proof/sealed:/sealed \
    gsc-my-proof
   ```

## Customization

Feel free to modify any part of this template to fit your specific needs. The goal is to provide a starting point that can be easily adapted to various proof tasks.

## Contributing

If you have suggestions for improving this template, please open an issue or submit a pull request.

## License

[MIT License](LICENSE)