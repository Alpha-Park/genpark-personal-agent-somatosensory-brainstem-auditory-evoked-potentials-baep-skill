"""
Example usage for Somatosensory Brainstem Auditory Evoked Potentials (BAEP / ABR) Skill.
"""

from client import BrainstemAuditoryEvokedPotentialsClient


def main():
    client = BrainstemAuditoryEvokedPotentialsClient()

    print("--- Case 1: Normal Bilateral Auditory Brainstem Conduction ---")
    normal_case = client.evaluate_baep(
        wave_i_latency_ms=1.62,
        wave_iii_latency_ms=3.78,
        wave_v_latency_ms=5.65,
        wave_i_amplitude_uv=0.38,
        wave_v_amplitude_uv=0.62,
        contralateral_wave_v_latency_ms=5.60,
        patient_age_years=36
    )
    print("IPL I-III (Lower Pontine):", normal_case["interpeak_latencies_ms"]["ipl_i_iii_lower_pontine_ms"], "ms")
    print("IPL III-V (Upper Pontine):", normal_case["interpeak_latencies_ms"]["ipl_iii_v_rostral_pontine_ms"], "ms")
    print("IPL I-V (Central Auditory CACT):", normal_case["interpeak_latencies_ms"]["ipl_i_v_central_auditory_cact_ms"], "ms")
    print("V/I Amplitude Ratio:", normal_case["comparative_metrics"]["wave_v_i_amplitude_ratio"])
    print("Neuro Status:", normal_case["clinical_assessment"]["neurophysiological_status"])
    print("Pathophysiology:", normal_case["clinical_assessment"]["pathophysiology_summary"])
    print()

    print("--- Case 2: Unilateral Retrocochlear Delay (Acoustic Neuroma) ---")
    neuroma_case = client.evaluate_baep(
        wave_i_latency_ms=1.65,
        wave_iii_latency_ms=4.30,
        wave_v_latency_ms=6.35,
        contralateral_wave_v_latency_ms=5.65,
        patient_age_years=48
    )
    print("IPL I-III:", neuroma_case["interpeak_latencies_ms"]["ipl_i_iii_lower_pontine_ms"], "ms")
    print("Interaural Wave V Delta (ILD):", neuroma_case["comparative_metrics"]["interaural_wave_v_latency_diff_ms"], "ms")
    print("Neuro Status:", neuroma_case["clinical_assessment"]["neurophysiological_status"])
    print("Pathophysiology:", neuroma_case["clinical_assessment"]["pathophysiology_summary"])
    print()

    print("--- Case 3: Pontomesencephalic Multiple Sclerosis Plaque ---")
    ms_case = client.evaluate_baep(
        wave_i_latency_ms=1.60,
        wave_iii_latency_ms=3.75,
        wave_v_latency_ms=6.15,
        wave_i_amplitude_uv=0.40,
        wave_v_amplitude_uv=0.15,
        patient_age_years=32
    )
    print("IPL III-V:", ms_case["interpeak_latencies_ms"]["ipl_iii_v_rostral_pontine_ms"], "ms")
    print("V/I Ratio:", ms_case["comparative_metrics"]["wave_v_i_amplitude_ratio"])
    print("Neuro Status:", ms_case["clinical_assessment"]["neurophysiological_status"])
    print("Pathophysiology:", ms_case["clinical_assessment"]["pathophysiology_summary"])


if __name__ == "__main__":
    main()
