# Issue Summary

From 7:00 pm to 10:00 pm, we received messages from users indicating that the platform was operating slowly. Although users could access the requested resources, the load was carried out very slowly, affecting the user experience and leading users to use other platforms. About 15% of our users sent us complaints about it. Based on our monitoring system, it was determined that the percentage of affected users could be 80%.

# Timeline

7:00 pm - First complaint that our website was slow
7:15 pm - Various complaints about a slowdown on our website
7:33 pm - Our support team began to communicate the case to the SRE
7:43 pm - The SRE began to review the problem to generate a preliminary report
8:30 pm - His conclusion: the primary server crashed and sent all requests to the backup server, which could not handle the volume of traffic.
9:00 pm-The cause seemed to occur because the new cleaning lady (Rosita) in her daily work wanted to clean the SRE's desk and spilled a glass of water on the table, a liquid that reached the server.
9:15 pm - We use another computer where we start the server automating the tasks with Docker.
10:15 pm: The server is running, although it is not a permanent solution, it will solve the problem.
10:20 pm - We informed users that our platform was up and running again

# Root Cause

That fateful day our SRE left his desk for a moment while going to the bathroom, on the way he got distracted with a co-worker, at which point Rosita entered the office and did a toilet, spilled the liquid and did not report on it, Rosita dried All so that when the SRE returned, it did not notice such a fact, days later they began to receive complaints from users. Therefore, our SRE in turn made the server deployment again solving the problem, unfortunately Rosita does not continue working with us after the event.

# Corrective measures

Block access to unauthorized personnel to the company's computing area.

Establish daily reviews of the performance and metrics of the servers.

Generate daily reports on the stability and operability of the platforms.

Admonish the SRE in charge for not securing the door of his office and for wasting time during office hours.
