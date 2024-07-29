# Prerequisites

- Valid AWS credentials with permissions to access the bucket. 

# Running the script

Execute the following to create a virtual environment:
```sh
VENV_DIR=./venv
python3 -m venv $VENV_DIR
```

To activate the virtual environment:

```sh
source $VENV_DIR/bin/activate
```

To install the required packages:

```sh
pip install -r requirements.txt
```

To run the script:

```sh
python3 -m main your-s3-bucket-name "your substring"
```

Help for the program is also available through:

```sh
python3 -m main --help
```

Sample arguments:

```sh
python3 -m main your-s3-bucket-name "your substring"  --s3_object_prefix /test/

python3 -m main your-s3-bucket-name "your substring"  --s3_object_prefix /test/ --result_output_file_path ./result.json
```