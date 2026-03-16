export default {
  async fetch(request, env) {
    if (request.method === 'OPTIONS') {
      return new Response(null, {
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'POST, OPTIONS',
          'Access-Control-Allow-Headers': 'Content-Type',
          'Access-Control-Max-Age': '86400',
        },
      });
    }

    if (request.method !== 'POST') {
      return new Response('Method not allowed', { status: 405 });
    }

    try {
      const { question } = await request.json();
      if (!question || typeof question !== 'string' || question.length > 500) {
        return json({ answer: Math.random() < 0.5 ? 'yes' : 'no' });
      }

      const res = await fetch('https://api.anthropic.com/v1/messages', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': env.ANTHROPIC_API_KEY,
          'anthropic-version': '2023-06-01',
        },
        body: JSON.stringify({
          model: 'claude-sonnet-4-20250514',
          max_tokens: 20,
          system: 'You are Bit from TRON. You can ONLY answer YES or NO. For yes/no questions, answer directly. For two-choice questions like "A or B?", pick one: first option = YES, second option = NO. Respond with ONLY the JSON: {"answer":"yes"} or {"answer":"no"}',
          messages: [{ role: 'user', content: question }],
        }),
      });

      if (!res.ok) {
        return json({ answer: Math.random() < 0.5 ? 'yes' : 'no' });
      }

      const data = await res.json();
      const text = (data.content?.[0]?.text || '').toLowerCase();
      const answer = text.includes('"no"') ? 'no' : 'yes';
      return json({ answer });
    } catch {
      return json({ answer: Math.random() < 0.5 ? 'yes' : 'no' });
    }
  },
};

function json(obj) {
  return new Response(JSON.stringify(obj), {
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
    },
  });
}
