

import { apiFetch, clearToken, setToken } from '../services/api.js';
import { $, escapeHtml, formatDate } from '../utils/dom.js';
import { toast } from '../components/toast.js';

let selectedJobId = null;

const STAGES = [
  {
    key: 'stage_1',
    title: 'Stage 1 - Intent Extraction',
    description: 'Structured JSON extracted from the instruction.',
  },
  {
    key: 'stage_2',
    title: 'Stage 2 - Object Localization',
    description: 'Bounding box and confidence for the target object.',
  },
  {
    key: 'stage_3',
    title: 'Stage 3 - Segmentation',
    description: 'Mask and preview generated from the localized box.',
  },
  {
    key: 'stage_4',
    title: 'Stage 4 - AI Inpainting',
    description: 'Final edited image produced by the pipeline.',
  },
  {
    key: 'final_output',
    title: 'Final Output',
    description: 'Stored result shown at the end of the pipeline.',
  },
];

function setStatus(text) {
  $('#authStatus').textContent = text;
}

function renderMetrics(metrics) {
  $('#metrics').innerHTML = `
    <div class="stat"><strong>${metrics.cpu_usage_percent}%</strong><span class="muted">CPU usage</span></div>
    <div class="stat"><strong>${metrics.ram_usage_mb} MB</strong><span class="muted">RAM usage</span></div>
    <div class="stat"><strong>${metrics.queue_size}</strong><span class="muted">Queue size</span></div>
    <div class="stat"><strong>${metrics.active_jobs}</strong><span class="muted">Active jobs</span></div>
  `;
}

function safeStringify(value) {
  if (value === null || value === undefined || value === '') return 'No output yet.';
  if (typeof value === 'string') return value;
  try {
    return JSON.stringify(value, null, 2);
  } catch {
    return String(value);
  }
}

function getJobPreviewUrl(job) {
  if (!job || job.status !== 'completed' || !job.id) return '';
  return `/generated/job_${String(job.id).padStart(8, '0')}.png`;
}

function renderStage1Workbench(job) {
  const stage1 = job.stage_trace?.stage_1 || null;
  const inputInstruction = stage1?.input?.instruction || job.instruction || 'No instruction available.';
  const output = stage1?.output || null;
  const handoff = stage1?.handoff || null;
  $('#stage1Badge').textContent = stage1?.status === 'completed' ? 'Stage 1 complete' : 'Stage 1 pending';
  $('#stage1Workbench').innerHTML = `
    <div class="grid-2">
      <div class="stage-workbench-box">
        <div class="badge">Input</div>
        <h3>Instruction and parse summary</h3>
        <div class="muted">${escapeHtml(stage1?.summary || 'Waiting for Stage 1 output.')}</div>
        <div class="stage-workbench-field">
          <span class="muted">Instruction</span>
          <p>${escapeHtml(inputInstruction)}</p>
        </div>
        <div class="stage-workbench-field">
          <span class="muted">Model</span>
          <p>${escapeHtml(stage1?.model || 'Qwen2.5-3B-Instruct GGUF')}</p>
        </div>
        <div class="stage-workbench-field">
          <span class="muted">Mode</span>
          <p>${escapeHtml(stage1?.prompt_mode || 'grammar-constrained JSON')}</p>
        </div>
      </div>
      <div class="stage-workbench-box">
        <div class="badge">Response Output</div>
        <h3>Stage 1 JSON payload</h3>
        <pre class="stage-json">${escapeHtml(safeStringify(output))}</pre>
        <div class="stage-workbench-field">
          <span class="muted">Handoff to Stage 2</span>
          <p>${handoff ? escapeHtml(`${handoff.next_stage}: ${handoff.target_object || 'n/a'}`) : 'Awaiting Stage 1 output.'}</p>
        </div>
        <div class="stage-handoff-grid">
          <div class="stage-handoff-chip"><span>Action</span><strong>${escapeHtml(handoff?.action || 'n/a')}</strong></div>
          <div class="stage-handoff-chip"><span>Target</span><strong>${escapeHtml(handoff?.target_object || 'n/a')}</strong></div>
          <div class="stage-handoff-chip"><span>Replacement</span><strong>${escapeHtml(handoff?.replacement_object || 'n/a')}</strong></div>
        </div>
      </div>
    </div>
  `;
}

function renderStageOutput(job, stageKey, stageData) {
  if (!stageData && stageKey !== 'final_output') {
    return '<div class="muted">No output recorded yet.</div>';
  }

  if (stageKey === 'stage_1') {
    return `
      <div class="muted">${escapeHtml(stageData.summary || '')}</div>
      <pre class="stage-json">${escapeHtml(safeStringify(stageData.output))}</pre>
    `;
  }

  if (stageKey === 'stage_2') {
    const output = stageData.output || {};
    return `
      <div class="muted">${escapeHtml(stageData.summary || '')}</div>
      <pre class="stage-json">${escapeHtml(safeStringify(output))}</pre>
      <div class="muted">Confidence: ${output.confidence ?? 'n/a'}</div>
    `;
  }

  if (stageKey === 'stage_3') {
    const output = stageData.output || {};
    const maskUrl = `/masks/job_${String(job.id).padStart(8, '0')}_mask.png`;
    const previewUrl = `/masks/job_${String(job.id).padStart(8, '0')}_mask_preview.png`;
    return `
      <div class="stage-preview-grid">
        <a class="stage-preview-link" href="${maskUrl}" target="_blank" rel="noreferrer">
          <img src="${previewUrl}" alt="Mask preview for job ${job.id}">
        </a>
      </div>
      <div class="muted">${escapeHtml(stageData.summary || '')}</div>
      <pre class="stage-json">${escapeHtml(safeStringify(output))}</pre>
    `;
  }

  if (stageKey === 'stage_4') {
    const output = stageData.output || {};
    const generatedUrl = getJobPreviewUrl(job) || `/generated/job_${String(job.id).padStart(8, '0')}.png`;
    return generatedUrl ? `
      <div class="stage-preview-grid">
        <a class="stage-preview-link" href="${generatedUrl}" target="_blank" rel="noreferrer">
          <img src="${generatedUrl}" alt="Final edited image for job ${job.id}">
        </a>
      </div>
      <div class="muted">${escapeHtml(stageData.summary || '')}</div>
      <pre class="stage-json">${escapeHtml(safeStringify(output))}</pre>
    ` : '<div class="muted">Final image is not available yet.</div>';
  }

  const generatedUrl = getJobPreviewUrl(job);
  return generatedUrl ? `
    <div class="stage-preview-grid">
      <a class="stage-preview-link" href="${generatedUrl}" target="_blank" rel="noreferrer">
        <img src="${generatedUrl}" alt="Final output preview for job ${job.id}">
      </a>
    </div>
    <div class="muted">${escapeHtml(job.output_path || generatedUrl)}</div>
  ` : '<div class="muted">Final output is not available yet.</div>';
}

function renderStageGrid(job) {
  const trace = job.stage_trace || {};
  renderStage1Workbench(job);
  $('#pipelineSummary').textContent = job.id ? `Job #${job.id} - ${job.status} - ${job.progress}%` : 'Awaiting job selection';
  $('#selectedJobMeta').textContent = job.id ? `Job #${job.id} - ${formatDate(job.created_at)}` : 'No job selected';
  $('#stageGrid').innerHTML = STAGES.map((stage) => {
    const stageData = stage.key === 'final_output'
      ? (job.output_path ? { summary: 'Final output stored on disk.', output: { output_path: job.output_path } } : null)
      : trace[stage.key] || null;
    const status = stageData?.status || (stage.key === 'final_output' ? (job.output_path ? 'available' : 'pending') : 'pending');
    return `
      <article class="stage-card ${stageData ? 'stage-card--ready' : 'stage-card--empty'}">
        <div class="stage-card-head">
          <div>
            <h3>${stage.title}</h3>
            <p class="muted">${stage.description}</p>
          </div>
          <span class="badge">${escapeHtml(status)}</span>
        </div>
        <div class="stage-card-body">
          ${renderStageOutput(job, stage.key, stageData)}
        </div>
      </article>
    `;
  }).join('');
}

function renderJobTable(jobs) {
  $('#recentJobs').innerHTML = jobs.map((job) => `
    <tr class="job-row ${job.id === selectedJobId ? 'job-row--selected' : ''}" data-job-id="${job.id}">
      <td>#${job.id}</td>
      <td>${escapeHtml(job.status)}</td>
      <td>${escapeHtml(job.instruction)}</td>
      <td>${job.progress}%</td>
    </tr>
  `).join('') || '<tr><td colspan="4" class="muted">No jobs yet.</td></tr>';

  $('#recentJobs').querySelectorAll('[data-job-id]').forEach((row) => {
    row.addEventListener('click', () => {
      const jobId = Number(row.getAttribute('data-job-id'));
      const job = jobs.find((item) => item.id === jobId);
      if (!job) return;
      selectedJobId = job.id;
      renderJobTable(jobs);
      renderStageGrid(job);
    });
  });
}

async function loadDashboard() {
  try {
    const [metrics, history] = await Promise.all([
      apiFetch('/metrics'),
      apiFetch('/history'),
    ]);
    renderMetrics(metrics);
    const jobs = history.jobs || [];
    renderJobTable(jobs);
    const selectedJob = jobs.find((job) => job.id === selectedJobId) || jobs[0] || null;
    if (selectedJob) {
      selectedJobId = selectedJob.id;
      renderStageGrid(selectedJob);
    } else {
      renderStageGrid({ id: 0, status: 'idle', progress: 0, created_at: new Date().toISOString(), output_path: '', stage_trace: {} });
    }
  } catch (error) {
    $('#authStatus').textContent = error.message;
  }
}

async function login() {
  const username = $('#username').value.trim();
  const password = $('#password').value;
  try {
    const result = await apiFetch('/auth/login', {
      method: 'POST',
      body: JSON.stringify({ username, password }),
    });
    setToken(result.access_token);
    setStatus(`Logged in as ${result.username} (${result.role})`);
    await loadDashboard();
  } catch (error) {
    clearToken();
    setStatus(error.message);
    toast(error.message, 'error');
  }
}

window.addEventListener('DOMContentLoaded', () => {
  $('#loginBtn').addEventListener('click', login);
  loadDashboard();
});
