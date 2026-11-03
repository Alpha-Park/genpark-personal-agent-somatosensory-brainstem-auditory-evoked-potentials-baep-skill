"""
MCP Server implementation for Somatosensory Brainstem Auditory Evoked Potentials (BAEP / ABR) Skill.
Exposes standard FastMCP-compatible tools for auditory brainstem and retrocochlear pathway conduction analysis.
"""

import sys
import json
from typing import Dict, Any, Optional
from client import BrainstemAuditoryEvokedPotentialsClient


def evaluate_brainstem_auditory_evoked_potentials(
    wave_i_latency_ms: float,
    wave_iii_latency_ms: float,
    wave_v_latency_ms: float,
    wave_i_amplitude_uv: Optional[float] = None,
    wave_v_amplitude_uv: Optional[float] = None,
    contralateral_wave_v_latency_ms: Optional[float] = None,
    stimulus_rate_hz: Optional[float] = 11.1,
    stimulus_intensity_db_nhl: Optional[float] = 75.0,
    patient_age_years: Optional[int] = 45
) -> str:
    """
    Evaluates Brainstem Auditory Evoked Potentials (BAEP) absolute and interpeak latencies.
    Returns structured analysis of retrocochlear vs brainstem conduction delay.
    """
    client = BrainstemAuditoryEvokedPotentialsClient()
    result = client.evaluate_baep(
        wave_i_latency_ms=wave_i_latency_ms,
        wave_iii_latency_ms=wave_iii_latency_ms,
        wave_v_latency_ms=wave_v_latency_ms,
        wave_i_amplitude_uv=wave_i_amplitude_uv,
        wave_v_amplitude_uv=wave_v_amplitude_uv,
        contralateral_wave_v_latency_ms=contralateral_wave_v_latency_ms,
        stimulus_rate_hz=stimulus_rate_hz,
        stimulus_intensity_db_nhl=stimulus_intensity_db_nhl,
        patient_age_years=patient_age_years
    )
    return json.dumps(result, indent=2)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--tools":
        tools = [
            {
                "name": "evaluate_brainstem_auditory_evoked_potentials",
                "description": "Calculates BAEP / ABR absolute latencies (Wave I, III, V), interpeak latencies (I-III, III-V, I-V CACT), interaural latency difference (ILD), and V/I amplitude ratio.",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "wave_i_latency_ms": {"type": "number", "description": "Wave I latency in ms (normal: 1.4 - 1.8 ms)"},
                        "wave_iii_latency_ms": {"type": "number", "description": "Wave III latency in ms (normal: 3.6 - 4.1 ms)"},
                        "wave_v_latency_ms": {"type": "number", "description": "Wave V latency in ms (normal: 5.4 - 6.0 ms)"},
                        "wave_i_amplitude_uv": {"type": "number", "description": "Optional Wave I amplitude in uV"},
                        "wave_v_amplitude_uv": {"type": "number", "description": "Optional Wave V amplitude in uV"},
                        "contralateral_wave_v_latency_ms": {"type": "number", "description": "Optional contralateral ear Wave V latency in ms for ILD calculation"},
                        "stimulus_rate_hz": {"type": "number", "description": "Stimulus click presentation frequency in Hz (default: 11.1 Hz)"},
                        "stimulus_intensity_db_nhl": {"type": "number", "description": "Click intensity in dB nHL (default: 75 dB)"},
                        "patient_age_years": {"type": "integer", "description": "Patient age in years (default: 45)"}
                    },
                    "required": ["wave_i_latency_ms", "wave_iii_latency_ms", "wave_v_latency_ms"]
                }
            }
        ]
        print(json.dumps(tools, indent=2))
    else:
        # Simple self-test
        client = BrainstemAuditoryEvokedPotentialsClient()
        test_res = client.evaluate_baep(
            wave_i_latency_ms=1.62,
            wave_iii_latency_ms=3.80,
            wave_v_latency_ms=5.65,
            wave_i_amplitude_uv=0.35,
            wave_v_amplitude_uv=0.55
        )
        print("Self-test passed:")
        print(json.dumps(test_res, indent=2))
