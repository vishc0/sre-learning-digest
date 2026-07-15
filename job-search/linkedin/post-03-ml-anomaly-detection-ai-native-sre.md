# Post 3: ML Anomaly Detection — AI-Native SRE

---

I built an ML anomaly detection system before I knew what MLOps was. Here is what I learned.

The year was not 2024. We were not using ChatGPT. We were using Splunk MLTK, a few Python scripts, and a lot of trial and error on a production platform processing millions of events per day.

The goal was simple: stop paging engineers for things that were not actually problems. Alert fatigue was real. Engineers were making judgment calls at 3am on alerts they had seen hundreds of times. Some of those calls were wrong.

So we trained anomaly models on baseline traffic patterns — time-of-day seasonality, day-of-week cycles, event correlation windows. The system learned what "normal" looked like and flagged deviations that the threshold-based alerts missed entirely. Not louder alerts. Smarter ones.

What I did not know at the time: I was doing feature engineering, model drift monitoring, and threshold tuning. I just called it "fixing the dashboards."

The lesson that matters now, in the era of AI-native SRE: the hardest part of applying ML to operations is not the model. It is curating the signal. Garbage telemetry produces confident wrong answers. An ML system trained on noisy data does not fail loudly — it fails quietly, and you trust it.

AI changes what SRE engineers build. It does not change the requirement to understand your data before you automate decisions on it.

Where in your on-call workflow are you most tempted to add AI before the signal is clean?

#SRE #AIforSRE #AnomalyDetection #Observability #MLOps #DevOps #PlatformEngineering
