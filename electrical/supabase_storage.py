import os
import uuid
from supabase import create_client

def get_supabase_client():
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")

    if not supabase_url:
        raise ValueError("SUPABASE_URL is missing")
    if not supabase_key:
        raise ValueError("SUPABASE_KEY is missing")

    return create_client(supabase_url, supabase_key)

def upload_image_to_supabase(uploaded_file):
    supabase = get_supabase_client()
    bucket = os.getenv("SUPABASE_BUCKET", "images")

    ext = uploaded_file.name.split(".")[-1].lower()
    file_name = f"projects/{uuid.uuid4()}.{ext}"

    file_bytes = uploaded_file.read()

    supabase.storage.from_(bucket).upload(
        path=file_name,
        file=file_bytes,
        file_options={
            "content-type": uploaded_file.content_type,
            "upsert": "false",
        },
    )

    return supabase.storage.from_(bucket).get_public_url(file_name)