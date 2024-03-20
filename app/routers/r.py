"""
Code from [devgoldy.xyz](https://github.com/THEGOLDENPRO/devgoldy.xyz/)
"""

from __future__ import annotations

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from fastapi.exceptions import HTTPException

from ..config import Config

__all__ = ("redirect", )

config = Config()
redirect = APIRouter()
templates = Jinja2Templates(directory = "./temp")

@redirect.get("/github")
async def github(request: Request):
    return templates.TemplateResponse(
        "redirect.html", {
            "request": request,
            "title": "My GitHub",
            "description": "Check out my open-source work at GitHub!",
            "image_url": "https://avatars.githubusercontent.com/u/66202304",
            "url": "https://github.com/R3tr0Ananas"
        }
    )

@redirect.get("/r/{redirect_id}")
async def custom(request: Request, redirect_id: str):
    print(redirect_id)
    redirects = await config.get_redirects()

    for redirect in redirects:

        if redirect["id"] == redirect_id:

            return templates.TemplateResponse(
                "redirect.html", {
                    "request": request,
                    "title": redirect["title"],
                    "description": redirect["description"],
                    "image_url": redirect["image_url"],
                    "url": redirect["url"]
                }
            )

    raise HTTPException(404)