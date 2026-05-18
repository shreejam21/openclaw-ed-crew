"""OPENCLAW-ED Crew — five-agent ED Command Center routed through OpenClaw's
OpenAI-compatible chat completions endpoint (which uses gotlu's
github-copilot/claude-opus-4.7 license)."""
from __future__ import annotations

import os

from crewai import Agent, Crew, LLM, Process, Task
from crewai.project import CrewBase, agent, crew, task


def _openclaw_llm() -> LLM:
    """LLM bound to OpenClaw's /v1/chat/completions endpoint."""
    base_url = os.getenv("OPENAI_API_BASE", "http://127.0.0.1:18790/v1")
    api_key = os.getenv("OPENAI_API_KEY", "openclaw-local")
    # hosted_vllm = OpenAI-compatible provider that accepts ANY model name and
    # honors a custom base_url. Avoids OpenAI's strict model-id validation.
    return LLM(
        model="hosted_vllm/openclaw",
        base_url=base_url,
        api_key=api_key,
    )


@CrewBase
class OpenclawEdCrew:
    """OPENCLAW-ED Command Center crew."""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def triage_risk_scorer(self) -> Agent:
        return Agent(
            config=self.agents_config["triage_risk_scorer"],
            llm=_openclaw_llm(),
            verbose=False,
        )

    @agent
    def sepsis_bundle_watcher(self) -> Agent:
        return Agent(
            config=self.agents_config["sepsis_bundle_watcher"],
            llm=_openclaw_llm(),
            verbose=False,
        )

    @agent
    def results_tracker(self) -> Agent:
        return Agent(
            config=self.agents_config["results_tracker"],
            llm=_openclaw_llm(),
            verbose=False,
        )

    @agent
    def discharge_optimizer(self) -> Agent:
        return Agent(
            config=self.agents_config["discharge_optimizer"],
            llm=_openclaw_llm(),
            verbose=False,
        )

    @agent
    def charge_coordinator(self) -> Agent:
        return Agent(
            config=self.agents_config["charge_coordinator"],
            llm=_openclaw_llm(),
            verbose=False,
        )

    @task
    def triage_task(self) -> Task:
        return Task(config=self.tasks_config["triage_task"])

    @task
    def sepsis_task(self) -> Task:
        return Task(config=self.tasks_config["sepsis_task"])

    @task
    def results_task(self) -> Task:
        return Task(config=self.tasks_config["results_task"])

    @task
    def discharge_task(self) -> Task:
        return Task(config=self.tasks_config["discharge_task"])

    @task
    def coordinator_task(self) -> Task:
        return Task(config=self.tasks_config["coordinator_task"])

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=False,
        )
