"""
Somatosensory Brainstem Auditory Evoked Potentials (BAEP / ABR) Conduction Client.
Zero-mock pure Python standard library implementation.
Calculates Wave I, III, V absolute latencies (ms), I-III, III-V, I-V interpeak latencies (IPL in ms),
Interaural Latency Difference (ILD in ms), and V/I amplitude ratio according to clinical neurophysiology standards.
"""

import math
from typing import Dict, Any, Optional


class BrainstemAuditoryEvokedPotentialsClient:
    """
    Evaluates auditory brainstem and retrocochlear pathway conduction:
    - Wave I Latency (ms): auditory nerve (normal: 1.40 - 1.80 ms)
    - Wave III Latency (ms): superior olivary complex / lower pons (normal: 3.60 - 4.10 ms)
    - Wave V Latency (ms): inferior colliculus / midbrain (normal: 5.40 - 6.00 ms)
    - IPL I-III (ms): caudal pontine conduction (normal: 2.00 - 2.40 ms)
    - IPL III-V (ms): rostral pontomesencephalic conduction (normal: 1.70 - 2.10 ms)
    - IPL I-V (ms): central auditory conduction time CACT (normal: 3.80 - 4.30 ms)
    - Interaural Wave V Delay (ILD ms): normal <= 0.40 ms
    - Amplitude Ratio V/I: normal >= 0.50
    - Screens for vestibular schwannoma, pontine MS plaques, and brainstem ischemic injury.
    """

    def __init__(self):
        pass

    def evaluate_baep(
        self,
        wave_i_latency_ms: float,
        wave_iii_latency_ms: float,
        wave_v_latency_ms: float,
        wave_i_amplitude_uv: Optional[float] = None,
        wave_v_amplitude_uv: Optional[float] = None,
        contralateral_wave_v_latency_ms: Optional[float] = None,
        stimulus_rate_hz: Optional[float] = 11.1,
        stimulus_intensity_db_nhl: Optional[float] = 75.0,
        patient_age_years: Optional[int] = 45
    ) -> Dict[str, Any]:
        """
        Calculates BAEP / ABR absolute and interpeak latencies and ratios.
        wave_i_latency_ms: Wave I onset latency in ms (e.g. 1.62 ms).
        wave_iii_latency_ms: Wave III onset latency in ms (e.g. 3.80 ms).
        wave_v_latency_ms: Wave V onset latency in ms (e.g. 5.65 ms).
        """
        if wave_i_latency_ms <= 0 or wave_iii_latency_ms <= 0 or wave_v_latency_ms <= 0:
            raise ValueError("Wave latencies must be strictly positive.")
        if not (wave_i_latency_ms < wave_iii_latency_ms < wave_v_latency_ms):
            raise ValueError("Latencies must follow anatomical sequence: Wave I < Wave III < Wave V.")

        # Interpeak Latencies (IPL)
        ipl_i_iii = round(wave_iii_latency_ms - wave_i_latency_ms, 2)
        ipl_iii_v = round(wave_v_latency_ms - wave_iii_latency_ms, 2)
        ipl_i_v = round(wave_v_latency_ms - wave_i_latency_ms, 2)

        # Amplitude Ratio V / I
        v_i_ratio = None
        if wave_i_amplitude_uv and wave_v_amplitude_uv and wave_i_amplitude_uv > 0:
            v_i_ratio = round(wave_v_amplitude_uv / wave_i_amplitude_uv, 2)

        # Interaural Wave V Latency Difference (ILD)
        ild_wave_v = None
        if contralateral_wave_v_latency_ms is not None:
            ild_wave_v = round(abs(wave_v_latency_ms - contralateral_wave_v_latency_ms), 2)

        # Neurophysiological Classification:
        # Normal upper limits: IPL I-III <= 2.45 ms, IPL III-V <= 2.20 ms, IPL I-V <= 4.40 ms
        # Normal ILD Wave V <= 0.40 ms
        # Normal V/I ratio >= 0.50
        is_i_iii_prolonged = ipl_i_iii > 2.45
        is_iii_v_prolonged = ipl_iii_v > 2.20
        is_i_v_prolonged = ipl_i_v > 4.40
        is_ild_abnormal = (ild_wave_v is not None and ild_wave_v > 0.40)
        is_ratio_abnormal = (v_i_ratio is not None and v_i_ratio < 0.50)

        if is_ild_abnormal or (is_i_iii_prolonged and not is_iii_v_prolonged):
            neuro_status = "Retrocochlear Conduction Delay / Auditory Nerve Pathway Defect"
            pathophysiology = "Prolonged I-III interval or interaural wave V asymmetry > 0.4 ms; warrants investigation for cerebellopontine angle mass / vestibular schwannoma."
        elif is_iii_v_prolonged:
            neuro_status = "Rostral Pontomesencephalic Brainstem Conduction Delay"
            pathophysiology = "Prolonged III-V interpeak interval; indicates demyelinating plaque, microvascular ischemia, or compression in upper pons/midbrain."
        elif is_i_v_prolonged:
            neuro_status = "Diffuse Central Auditory Conduction Time (CACT) Prolongation"
            pathophysiology = "Extended global brainstem auditory pathway conduction; suggests diffuse central demyelination or neurodegenerative disorder."
        elif wave_i_latency_ms > 1.90 and not (is_i_iii_prolonged or is_iii_v_prolonged):
            neuro_status = "Peripheral Conductive or Cochlear Conduction Delay"
            pathophysiology = "Delayed wave I onset with preserved central interpeak intervals; typical of middle ear effusion or cochlear sensory hearing loss."
        elif is_ratio_abnormal:
            neuro_status = "Attenuated Wave V/I Amplitude Ratio"
            pathophysiology = "Wave V amplitude depressed relative to wave I (< 0.50); indicates brainstem desynchronization or central auditory fatigue."
        else:
            neuro_status = "Normal Brainstem Auditory Evoked Potential Conduction"
            pathophysiology = "Intact bilateral auditory nerve transmission and synchronized brainstem relay through cochlear nucleus, superior olive, and inferior colliculus."

        return {
            "status": "success",
            "absolute_latencies_ms": {
                "wave_i_latency_ms": round(wave_i_latency_ms, 2),
                "wave_iii_latency_ms": round(wave_iii_latency_ms, 2),
                "wave_v_latency_ms": round(wave_v_latency_ms, 2)
            },
            "interpeak_latencies_ms": {
                "ipl_i_iii_lower_pontine_ms": ipl_i_iii,
                "ipl_iii_v_rostral_pontine_ms": ipl_iii_v,
                "ipl_i_v_central_auditory_cact_ms": ipl_i_v
            },
            "comparative_metrics": {
                "wave_v_i_amplitude_ratio": v_i_ratio,
                "interaural_wave_v_latency_diff_ms": ild_wave_v
            },
            "recording_context": {
                "stimulus_rate_hz": stimulus_rate_hz,
                "stimulus_intensity_db_nhl": stimulus_intensity_db_nhl,
                "patient_age_years": patient_age_years
            },
            "clinical_assessment": {
                "neurophysiological_status": neuro_status,
                "pathophysiology_summary": pathophysiology
            }
        }
