from dotenv import load_dotenv
from huggingface_hub import InferenceClient

## You need a token from https://hf.co/settings/tokens. If you run this on Google Colab, you can set it up in the "settings" tab under "secrets". Make sure to call it "HF_TOKEN"
# os.environ["HF_TOKEN"]="hf_xxxxxxxxxxxxxx"
load_dotenv()

STR_DIV = "\n=====================\n"

client = InferenceClient("meta-llama/Llama-3.2-3B-Instruct")
# if the outputs for next cells are wrong, the free model may be overloaded. You can also use this public endpoint that contains Llama-3.2-3B-Instruct
# client = InferenceClient("https://jc26mwg228mkj8dw.us-east-1.aws.endpoints.huggingface.cloud")

example_prompts = [
    "The capital of France is",
    """<|begin_of_text|><|start_header_id|>user<|end_header_id|>
The capital of France is<|eot_id|><|start_header_id|>assistant<|end_header_id|>""",
]

for ind, prompt in enumerate(example_prompts):
    output = client.text_generation(
        prompt,
        max_new_tokens=100,
    )
    print(f"Prompt {ind} response{STR_DIV}{output.strip()}\n")

output = client.chat.completions.create(
    messages=[
        {"role": "user", "content": "The capital of France is"},
    ],
    stream=False,
    max_tokens=1024,
)
print(f"Prompt 3 response{STR_DIV}{output.choices[0].message.content}\n")
