from kaneda import Metrics


class TestQueues(object):

    def test_benchmark_celery(self, celery_queue, benchmark):
        metrics = Metrics(queue=celery_queue)
        benchmark(metrics.gauge, 'benchmark_celery', 1)

    def test_benchmark_rq(self, rq_queue, benchmark):
        metrics = Metrics(queue=rq_queue)
        benchmark(metrics.gauge, 'benchmark_rq', 1)
