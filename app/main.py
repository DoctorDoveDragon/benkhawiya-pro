"""
BENKHAWIYA AI - PROFESSIONAL COSMIC REASONING API
Deployable to sacredtreeofthephoenix.org
"""

from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from contextlib import asynccontextmanager
import logging
import os
from typing import Dict, Any
from pathlib import Path

from app.core.cosmic_engine import BenkhawiyaEngine, CouncilAspect, CosmicDecision

# Professional logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Templates
templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))

# Global engine instance
cosmic_engine = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    global cosmic_engine
    logger.info("🌌 INITIALIZING BENKHAWIYA COSMIC REASONING SYSTEM")
    try:
        cosmic_engine = BenkhawiyaEngine()
        logger.info("✅ Cosmic engine initialized successfully")
    except Exception as e:
        logger.error(f"❌ Failed to initialize cosmic engine: {e}")
        cosmic_engine = None
    yield
    logger.info("🛑 Benkhawiya AI system shutting down")


app = FastAPI(
    title="Benkhawiya AI - Cosmic Reasoning System",
    description="Professional implementation for sacredtreeofthephoenix.org",
    version="2.0.0",
    lifespan=lifespan,
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_cosmic_engine() -> BenkhawiyaEngine:
    if cosmic_engine is None:
        raise HTTPException(status_code=503, detail="Cosmic reasoning engine unavailable")
    return cosmic_engine


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Serve the web UI"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/api", response_model=Dict[str, Any])
async def api_root():
    """API information endpoint"""
    return {
        "system": "Benkhawiya AI - Cosmic Reasoning System",
        "version": "2.0.0",
        "status": "operational" if cosmic_engine else "degraded",
        "domain": "sacredtreeofthephoenix.org",
        "features": {"council_reasoning": True, "cosmic_principles": True, "golden_ratio_mathematics": True},
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy" if cosmic_engine else "degraded",
        "components": {
            "cosmic_engine": cosmic_engine is not None,
            "principles_loaded": len(cosmic_engine.principles) if cosmic_engine else 0,
        },
    }


@app.get("/principles")
async def get_cosmic_principles(
    aspect: CouncilAspect = None, engine: BenkhawiyaEngine = Depends(get_cosmic_engine)
) -> Dict[str, Any]:
    principles = engine.get_principles_by_aspect(aspect) if aspect else engine.principles
    return {
        "count": len(principles),
        "aspect": aspect.value if aspect else "all",
        "principles": [principle.dict() for principle in principles],
    }


@app.post("/council/consult", response_model=CosmicDecision)
async def consult_council(
    question: str, context: Dict[str, Any] = None, engine: BenkhawiyaEngine = Depends(get_cosmic_engine)
) -> CosmicDecision:
    try:
        decision = await engine.consult_council(question, context)
        logger.info(f"Council consultation completed: {question[:50]}...")
        return decision
    except Exception as e:
        logger.error(f"Council consultation failed: {e}")
        raise HTTPException(status_code=500, detail=f"Cosmic reasoning failed: {str(e)}")


@app.get("/mathematics/golden-ratio/{n}")
async def calculate_golden_progression(n: int, engine: BenkhawiyaEngine = Depends(get_cosmic_engine)) -> Dict[str, Any]:
    if n < 0 or n > 100:
        raise HTTPException(status_code=400, detail="n must be between 0 and 100")

    progression = engine.calculate_golden_progression(n)

    return {
        "developmental_stage": n,
        "golden_ratio": engine.phi,
        "progression_value": progression,
        "description": f"Cosmic developmental progression at stage {n}",
    }


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    """Serve the favicon.ico file"""
    favicon_path = Path(__file__).parent / "static" / "favicon.ico"
    if favicon_path.exists():
        return FileResponse(favicon_path, media_type="image/x-icon")
    raise HTTPException(status_code=404, detail="Favicon not found")


if __name__ == "__main__":
    import uvicorn

    port = int(os.getenv("PORT", 8000))
    # Bind to 0.0.0.0 for deployment on cloud platforms (Railway, Heroku, etc.)
    uvicorn.run(app, host="0.0.0.0", port=port)  # nosec B104
