import os
import uuid
from supabase import create_client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET", "images")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_image_to_supabase(uploaded_file):
    ext = uploaded_file.name.split(".")[-1].lower()
    file_name = f"projects/{uuid.uuid4()}.{ext}"

    file_bytes = uploaded_file.read()

    supabase.storage.from_(SUPABASE_BUCKET).upload(
        path=file_name,
        file=file_bytes,
        file_options={
            "content-type": uploaded_file.content_type,
            "upsert": "false",
        },
    )

    public_url = supabase.storage.from_(SUPABASE_BUCKET).get_public_url(file_name)
    return public_url

