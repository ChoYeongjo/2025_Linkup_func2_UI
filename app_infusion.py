import streamlit as st
# only UI 일단 임시
st.title("💉CRS Risk Scan (Post-Infusion(24h))")
st.markdown("**CAR-T 세포 치료제** 주입 후, 추적 관찰 중 24시간 내 **중증 CRS** 발생 여부를 예측합니다.")

cols=st.columns(7)
cytokines = ["IL-2", "IL-4", "IL-6", "IL-10", "TNFα", "IFNγ", "IL-17A"]
cytokine_values = {}
for i, col in enumerate(cols):
    cytokine_values[cytokines[i]] = col.number_input(
        label=cytokines[i],
        min_value=0.0,
        max_value=100000.0,
        value=0.0,
        format="%.1f"
    )

st.write("사용자가입력한 사이토카인 수치:", cytokine_values)

if st.button("🔍현재 수치 기준 24시간 이내 환자의 중증 CRS 발생 가능성"):
  st.success(f"결과 출력칸-> 현재 수치 기준 24시간 이내 00.00% ")
