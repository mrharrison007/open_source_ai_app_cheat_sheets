# LLM Interface or WebUI Curl Test Commands

Reference: [OpenAI API](https://github.com/oobabooga/text-generation-webui/wiki/12-%E2%80%90-OpenAI-API)

## Completion

```
curl http://127.0.0.1:5000/v1/completions \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "This is a cake recipe:\n\n1.",
    "max_tokens": 200,
    "temperature": 1,
    "top_p": 0.9,
    "seed": 10
  }'
```

## Chat Completions

```
curl http://127.0.0.1:5000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "user",
        "content": "Hello, how is the weather where you are?"
      }
    ],
    "mode": "instruct",
    "instruction_template": "Alpaca"
  }'
```

## Chat completions with characters

```
curl http://127.0.0.1:5000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "user",
        "content": "Hello! Who are you?"
      }
    ],
    "mode": "chat",
    "character": "Example"
  }'
```

## SSE streaming

```
curl http://127.0.0.1:5000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [
      {
        "role": "user",
        "content": "Hello!"
      }
    ],
    "mode": "instruct",
    "instruction_template": "Alpaca",
    "stream": true
  }'
```

## Logits

```
curl -k http://127.0.0.1:5000/v1/internal/logits \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Who is best, Asuka or Rei? Answer:",
    "use_samplers": false
  }'
```

## Logits after sampling parameters

```
curl -k http://127.0.0.1:5000/v1/internal/logits \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Who is best, Asuka or Rei? Answer:",
    "use_samplers": true,
    "top_k": 3
  }'
```



## Large Parameter Curl Example

```
curl http://127.0.0.1:5000/v1/chat/completions \
-H "Content-Type: application/json" \
-d '{
  "messages": [
    {
      "role": "user",
      "content": "Give me a Hello World Script in Python"
    }
  ],
  "mode": "chat",
  "max_new_tokens": 512,
  "temperature": 0.7,
  "temperature_last": false,
  "dynamic_temperature": false,
  "dynatemp_low": 1,
  "dynatemp_high": 1,
  "dynatemp_exponent": 1,
  "smoothing_factor": 0,
  "top_p": 0.9,
  "min_p": 0,
  "top_k": 20,
  "repetition_penalty": 1.15,
  "presence_penalty": 0,
  "frequency_penalty": 0,
  "repetition_penalty_range": 1024,
  "typical_p": 1,
  "tfs": 1,
  "top_a": 0,
  "guidance_scale": 1,
  "penalty_alpha": 0,
  "mirostat_mode": 0,
  "mirostat_tau": 5,
  "mirostat_eta": 0.1,
  "do_sample": true,
  "encoder_repetition_penalty": 1,
  "no_repeat_ngram_size": 0,
  "min_length": 0,
  "num_beams": 1,
  "length_penalty": 1,
  "early_stopping": false,
  "sampler_priority": [
    "temperature",
    "dynamic_temperature",
    "quadratic_sampling",
    "top_k",
    "top_p",
    "typical_p",
    "epsilon_cutoff",
    "eta_cutoff",
    "tfs",
    "top_a",
    "min_p",
    "mirostat"
  ],
  "use_cache": true,
  "eos_token_id": [2]
}'

```

