import openai
from instagram_private_api import Client, ClientCompatPatch

# OpenAI API kimlik doğrulama anahtarınızı ayarlayın
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Instagram kimlik bilgilerinizi ayarlayın
username = 'YOUR_INSTAGRAM_USERNAME'
password = 'YOUR_INSTAGRAM_PASSWORD'

# OpenAI GPT-3 modeliyle metin üretme işlemi
def generate_text(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        echo=True
    )
    return response.choices[0].text.strip()

# Instagram hikaye paylaşma işlemi
def share_story(image_path, caption):
    api = Client(auto_patch=True, authenticate=True, username=username, password=password)
    api.post_photo(image_path, caption=caption)

# Hikaye oluşturma ve paylaşma işlemi
def create_and_share_story(prompt):
    generated_text = generate_text(prompt)
    image_path = 'PATH_TO_IMAGE'  # Yüklenecek hikaye resminin dosya yolu
    caption = generated_text
    share_story(image_path, caption)

# Kullanıcı giriş metnini alın ve hikaye oluşturma işlemini başlatın
user_prompt = input("Bir başlangıç metni girin: ")
create_and_share_story(user_prompt)
