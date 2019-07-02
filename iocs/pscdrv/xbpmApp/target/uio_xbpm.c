#include <linux/version.h>
#include <linux/device.h>
#include <linux/module.h>
#include <linux/platform_device.h>
#include <linux/uio_driver.h>
#include <linux/io.h>
#include <linux/interrupt.h>
#include <linux/delay.h>
#include <linux/slab.h>

#define DRV_VERSION "1"

MODULE_LICENSE("GPL v2");
MODULE_VERSION(DRV_VERSION);
MODULE_AUTHOR("Michael Davidsaver <mdavidsaver@bnl.gov>");

static ulong fpga_base = 0x10000000;
static ulong fpga_size = 0x10000000;

module_param_named(fpgabase, fpga_base, ulong, 0444);
module_param_named(fpgasize, fpga_size, ulong, 0444);

MODULE_PARM_DESC(fpga_base, "Start of FPGA DDR RAM");
MODULE_PARM_DESC(fpga_size, "Size of FPGA DDR RAM");

struct xbpm_dev {
    struct uio_info info;
};

static int xbpm_probe(struct platform_device *pdev)
{
    int ret;
    struct xbpm_dev *bdev;

    bdev = kzalloc(sizeof(*bdev), GFP_KERNEL);
    if(!bdev) return -ENOMEM;

    bdev->info.mem[0].name = "ddr";
    bdev->info.mem[0].addr = fpga_base;
    bdev->info.mem[0].size = fpga_size;
    bdev->info.mem[0].memtype = UIO_MEM_PHYS;

    bdev->info.name = "xbpm";
    bdev->info.version = DRV_VERSION;
    bdev->info.priv = bdev;

    ret = uio_register_device(&pdev->dev, &bdev->info);
    if(ret<0) {
        dev_err(&pdev->dev, "failed to register UIO\n");
    } else {
        platform_set_drvdata(pdev, bdev);
        dev_info(&pdev->dev, "Loaded XBPM DDR driver\n");
        ret = 0;
    }

    return ret;
}

static int xbpm_remove(struct platform_device *pdev)
{
    struct xbpm_dev *bdev = platform_get_drvdata(pdev);
    uio_unregister_device(&bdev->info);
    return 0;
}

static struct of_device_id xbpm_match[] = {
  {.compatible = "xlnx,zynq-7000", },
  {}
};

MODULE_DEVICE_TABLE(of, xbpm_match);

static struct platform_driver xbpm_driver = {
  .driver = {
    .name = "xbpm-ddr",
    .of_match_table = xbpm_match,
  },
  .probe = xbpm_probe,
  .remove = xbpm_remove,
};

module_platform_driver(xbpm_driver)
