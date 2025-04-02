import boto3

# Initialize Polly client
polly_client = boto3.client('polly', region_name='us-east-1')

# Text with SSML for enhanced speech
ssml_text = """<speak>
    Welcome to <emphasis level="strong">Real Estate Hub</emphasis>! 
    Here is a listing in <break time="500ms"/> New York.
    The price is <prosody rate="slow">$450,000</prosody>.
</speak>"""

# Convert text to speech
response = polly_client.synthesize_speech(
    Text=ssml_text,
    OutputFormat='mp3',
    TextType='ssml',
    VoiceId='Joanna'  # Choose from multiple available voices
)

# Save the speech output
with open("real_estate_voice.mp3", "wb") as file:
    file.write(response['AudioStream'].read())

print("🎧 Voice output saved successfully!")
